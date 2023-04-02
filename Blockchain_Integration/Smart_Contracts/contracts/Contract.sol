// SPDX-License-Identifier: GPL-3.0
pragma solidity >=0.4.16 <0.9.0;

contract HashStorage {
    //address owner;

    // constructor() {
    //     owner = msg.sender;
    // }

    struct userDetails {
        string firstName;
        string lastName;
        string email;
        bool exists;
    }

    //mapping (string => uint) public register;

    mapping(string => userDetails) public UserList;

    function insert_user(
        string memory user_id,
        string calldata FirstName,
        string calldata LastName
    ) public {
        if (!(UserList[user_id].exists)) {
            //register[user_id] = 1;
            userDetails memory newUser = userDetails({
                firstName: FirstName,
                lastName: LastName,
                email: user_id,
                exists: true
            });

            UserList[user_id] = newUser;
        }
    }

    function check_user(string memory user_id) public view returns (bool) {
        return UserList[user_id].exists;
    }

    // struct RequestDetails {
    //     string requested_id;
    //     uint256 image_id;
    // }

    // mapping (string => RequestDetails) public request_map;

    // function addRequest(string memory userId, string memory requestedId, uint256 imageId) public {
    //     RequestDetails memory newRequest = RequestDetails({
    //         requested_id: requestedId,
    //         image_id: imageId
    //     });
    //     request_map[userId] = newRequest;
    // }

    // function updateRequest(string memory userId, string memory requestedId, uint256 imageId) public {
    //     request_map[userId].requested_id = requestedId;
    //     request_map[userId].image_id = imageId;
    // }

    //Self Explanatory
    struct ImageDetails {
        string merkle_root;
        string url;
        string time_stamp;
        string caption;
        bool has_access;
        bool is_Sender;
    }

    //Person 2 struct, has 2 members : An array of image ids, (1-n) and a mapping that maps these ids to image details
    struct ImageStruct {
        uint256[] images;
        mapping(uint256 => ImageDetails) Images_Map;
    }

    //Person 1 struct, has 2 members : An array of names , and a mapping of names to Person 2 structs.
    struct ReceiverStruct {
        string[] Names;
        mapping(string => ImageStruct) Communications;
    }

    //Mapping with Person 1 -> Person 2 -> number of images shared between person 1 and person 2
    mapping(string => mapping(string => uint256)) public image_count;

    //Mapping with sender name as key, value is Sender struct.
    mapping(string => ReceiverStruct) internal Communication_Matrix;

    function grant_access(
        string calldata sender,
        string calldata receiver,
        uint256 idx
    ) public {
        Communication_Matrix[sender]
            .Communications[receiver]
            .Images_Map[idx]
            .has_access = true;
    }

    // Only image sender can grant/revoke access to receiver
    function revoke_access(
        string calldata sender,
        string calldata receiver,
        uint256 idx
    ) public {
        require(
            Communication_Matrix[sender]
                .Communications[receiver]
                .Images_Map[idx]
                .is_Sender == true,
            "Only the sender can modify access rights!"
        );
        Communication_Matrix[receiver]
            .Communications[sender]
            .Images_Map[idx]
            .has_access = false;
    }

    function construct_Image_Details(
        string calldata url,
        string calldata image_hash,
        string calldata time_stamp,
        string calldata caption
    ) public returns (ImageDetails memory obj) {
        ImageDetails memory details_data = ImageDetails({
            merkle_root: image_hash,
            url: url,
            time_stamp: time_stamp,
            has_access: true,
            is_Sender: true,
            caption: caption
        });

        return details_data;
    }

    //With given parameters, constructs the details struct and adds the image details to the image details map, with an auto incremented key

    function handleFirstTimeAdd(
        string calldata sender,
        string calldata receiver
    ) internal {
        if (image_count[sender][receiver] == 0) {
            Communication_Matrix[sender].Names.push(receiver);
            Communication_Matrix[receiver].Names.push(sender);
        }
    }

    function addToMatrix(
        string calldata sender,
        string calldata receiver,
        ImageDetails memory details_data
    ) internal {
        Communication_Matrix[sender].Communications[receiver].images.push(
            ++image_count[sender][receiver]
        );
        Communication_Matrix[receiver].Communications[sender].images.push(
            ++image_count[receiver][sender]
        );
        Communication_Matrix[sender].Communications[receiver].Images_Map[
            image_count[sender][receiver]
        ] = details_data;
        details_data.is_Sender = false;
        Communication_Matrix[receiver].Communications[sender].Images_Map[
            image_count[receiver][sender]
        ] = details_data;
    }

    function add_image_details(
        string calldata sender,
        string calldata receiver,
        string calldata url,
        string calldata image_hash,
        string calldata time_stamp,
        string calldata caption
    ) public {
        ImageDetails memory details_data = construct_Image_Details(
            url,
            image_hash,
            time_stamp,
            caption
        );

        {
            handleFirstTimeAdd(sender, receiver);
        }
        {
            addToMatrix(sender, receiver, details_data);
        }
    }

    //  function get_latest_hash(string memory uid) public view returns (string memory)
    //  {

    //      uint256 latest_id = image_count[uid];

    //      require(access_list[uid][images[uid][latest_id]]==true,"Only sender and receiver can access");
    //      return images[uid][latest_id];
    //  }

    // all images shared b/w person a and person b
    function get_images_shared(
        string calldata sender,
        string calldata receiver
    ) public view returns (uint256[] memory, ImageDetails[] memory) {
        uint256[] memory idxs = Communication_Matrix[sender]
            .Communications[receiver]
            .images;
        uint256 l = idxs.length;
        ImageDetails[] memory img_details = new ImageDetails[](l);
        //img_details[i] = Sender_Receiver_Map[sender].Receivers[receiver].Images_Map[1];

        for (uint256 i = 0; i < idxs.length; i++)
            img_details[i] = Communication_Matrix[sender]
                .Communications[receiver]
                .Images_Map[i + 1];

        return (idxs, img_details);
    }

    // all people that a person has communicated with
    function get_Names(
        string memory sender_id
    ) public view returns (userDetails[] memory names) {
        userDetails[] memory users_communicated_with = new userDetails[](Communication_Matrix[sender_id].Names.length);
        for(uint256 i =0;i<Communication_Matrix[sender_id].Names.length;i++)
        {
            users_communicated_with[i] = UserList[Communication_Matrix[sender_id].Names[i]];
        }

        return users_communicated_with;
    }
    }
