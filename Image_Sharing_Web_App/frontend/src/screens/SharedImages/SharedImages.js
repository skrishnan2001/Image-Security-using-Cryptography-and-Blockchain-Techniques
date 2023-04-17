import React, { useState, useEffect } from "react";
import LockIcon from '@mui/icons-material/Lock';
import KeyIcon from '@mui/icons-material/Key';

const SharedImages = ({ sender, receiver }) => {

    const [data, setData] = useState([]);
    const [receiverData, setReceiverData] = useState([])

    //Inverse GET Call for fetching receiver's access privileges
    useEffect(() => {
        const fetchData1 = async () => {
            await fetch(`/${receiver}/communications/${sender}`).then(
                res => res.json()
            ).then(
                receiverData => {
                    setReceiverData(receiverData)
                    console.log(receiverData)
                }
            ).catch(err => {
                console.log(err)
            })
        };
        fetchData1();
    }, [sender, receiver])

    useEffect(() => {
        const fetchData2 = async () => {
            await fetch(`/${sender}/communications/${receiver}`).then(
                res => res.json()
            ).then(
                data => {
                    setData(data)
                    console.log(data)
                }
            ).catch(err => {
                console.log(err)
            })
        }
        fetchData2();
    }, [sender, receiver,])

    const accessControl = (type, imageId) => {
        const data = {
            "sender": sender,
            "user2": receiver,
            "idx": imageId,
            "access_type": type
        }

        console.log(JSON.stringify(data))

        fetch(`/${sender}/access`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(data)
        })
            .then(response => response.json())
            .then(data => {
                console.log('Success:', data);
            })
            .catch((error) => {
                console.error('Error:', error);
            });
    }

    return (
        <>{data && data.map((item, idx) => (
            <div className="card mt-5 mb-5 mx-auto" key={idx}>

                {(item.is_Sender || item.hasAccess) &&
                    <>
                        <img className="card-img-top" src={item.url} alt="Uploaded to IPFS" />
                        <div className="card-body">
                            <p className="card-text"><strong>Sender:  {item.is_Sender ? sender : receiver}</strong></p>
                            <p className="card-text">{item.caption}</p>
                            <p className="card-text text-success">Merkle Root Hash: <strong>{item.merkle_hash}</strong></p>
                            <p className="card-text">{item.timestamp}</p>
                            {item.is_Sender && receiverData && receiverData[item.image_id - 1] && receiverData[item.image_id - 1].hasAccess && <button type="button" className="btn btn-danger" onClick={() => accessControl('revoke', item.image_id)}><LockIcon /> Revoke Access</button>}
                            {item.is_Sender && receiverData && receiverData[item.image_id - 1] && !receiverData[item.image_id - 1].hasAccess && <button type="button" className="btn btn-success" onClick={() => accessControl('grant', item.image_id)}><KeyIcon /> Grant Access</button>}

                        </div>
                    </>
                }
            </div>
        ))}
        </>
    )
}

export default SharedImages;