import React from 'react'
import "./Loader.css";

function Loader() {
    return (
        <div>
            <div class="spinner-loading"></div>
            <h2 class="spinner-loader-text">Uploading to IPFS</h2>
        </div>
    )
}

export default Loader