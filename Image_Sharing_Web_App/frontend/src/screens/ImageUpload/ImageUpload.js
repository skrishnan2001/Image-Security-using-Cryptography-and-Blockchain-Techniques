import { useState } from 'react';
import { Button, Form } from 'react-bootstrap';
import Loader from '../../components/Loader/Loader';
import { encode as base64_encode } from 'base-64';
import AddPhotoAlternateIcon from '@mui/icons-material/AddPhotoAlternate';
import SendIcon from '@mui/icons-material/Send';

require('dotenv').config()
const IPFS = require('ipfs-api');

let secrets = process.env.REACT_APP_INFURA_PROJECT_ID + ':' + process.env.REACT_APP_INFURA_PROJECT_SECRET;
let encodedSecrets = base64_encode(secrets);
const ipfs = new IPFS({
    host: 'ipfs.infura.io', port: 5001, protocol: 'https', headers: {
        Authorization: 'Basic ' + encodedSecrets
    }
});

function ImageUpload() {
    const [buf, setBuf] = useState();
    const [hash, setHash] = useState("");
    const [loader, setLoader] = useState(false);
    const [showLinks, setShowLinks] = useState(false);

    const captureFile = (event) => {
        event.stopPropagation()
        event.preventDefault()
        const file = event.target.files[0]
        let reader = new window.FileReader()
        reader.readAsArrayBuffer(file)
        reader.onloadend = () => convertToBuffer(reader)
    };

    const convertToBuffer = async (reader) => {
        //file is converted to a buffer to prepare for uploading to IPFS
        const buffer = await Buffer.from(reader.result);
        setBuf(buffer);
    };
    const onSubmit = async (event) => {
        event.preventDefault();
        setLoader(true);
        let ipfsId
        const buffer = buf
        await ipfs.add(buffer)
            .then((response) => {
                ipfsId = response[0].hash
                console.log("Generated IPFS Hash: ", ipfsId)
                setHash(ipfsId);
            }).catch((err) => {
                console.error(err)
                alert('An error occurred. Please check the console');
            })
        if (ipfsId)
            setShowLinks(true)
        else
            setShowLinks(false)
        setLoader(false);
    }
    if (loader) {
        return (
            <Loader />
        )
    }
    return (
        <div>
            <div class="card">
                <h5 class="card-header">Send Image</h5>
                <div class="card-body">
                    <h5 class="card-title">Choose the image to be sent</h5>
                    <Form onSubmit={onSubmit}>
                        <AddPhotoAlternateIcon /> <input type="file" onChange={captureFile} required />
                        <div className="d-grid gap-2 mt-5">
                            <Button type="submit">  Send <SendIcon /> </Button>
                        </div>
                    </Form>
                </div>
            </div>

            {
                showLinks ?
                    <div class="card mt-5 mb-5 mx-auto">
                        <img class="card-img-top" src={"https://ipfs.io/ipfs/" + hash} alt="Uploaded to IPFS" />
                        <div class="card-body">
                            <p class="card-text text-success">IPFS Hash: <strong> {hash}</strong></p>
                            {/* <p>Non clickabe Link: https://ipfs.io/ipfs/{hash}</p> */}
                            <a href={"https://ipfs.io/ipfs/" + hash} target="_blank" rel="noopener noreferrer">Clickable Link to view file on IPFS</a>
                        </div>
                    </div> :
                    <p></p>
            }
        </div>
    );
}

export default ImageUpload;
