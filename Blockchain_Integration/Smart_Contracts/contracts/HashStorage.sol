// SPDX-License-Identifier: GPL-3.0
pragma solidity >=0.4.16 <0.9.0;

contract HashStorage {
    address owner;

    constructor() {
        owner = msg.sender;
    }

    mapping(string => uint256) public image_count;
    mapping(string => mapping(uint256 => string)) public images;

    function set(string calldata user_id, string calldata image_hash) public {
        uint256 curr_count = image_count[user_id];
        images[user_id][curr_count + 1] = image_hash;
        image_count[user_id] = curr_count + 1;
    }

    function get(string memory uid, uint256 idx)
        public
        view
        returns (string memory)
    {
        return images[uid][idx];
    }
}
