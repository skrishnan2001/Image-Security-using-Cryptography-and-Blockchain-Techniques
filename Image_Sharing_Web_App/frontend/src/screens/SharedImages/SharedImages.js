import React, { useState, useEffect } from "react";

const SharedImages = ({ sender, receiver }) => {

    const [data, setData] = useState([]);
    useEffect(() => {
        fetch(`/${sender}/communications/${receiver}`).then(
            res => res.json()
        ).then(
            data => {
                setData(data)
                console.log(data)
            }
        ).catch(err => {
            console.log(err)
        })
    }, [sender, receiver])

    return (
        <>{data.map((item, idx) => (
            <div className="card mt-5 mb-5 mx-auto" key={idx}>
                <img className="card-img-top" src={item.url} alt="Uploaded to IPFS" />
                <div className="card-body">
                    <p className="card-text"><strong>{item.caption}</strong></p>
                    <p className="card-text text-success">Merkle Root Hash: <strong>{item.merkle_hash}</strong></p>
                    <p className="card-text">{item.timestamp}</p>
                </div>
            </div>
        ))}
        </>
    )
}

export default SharedImages;