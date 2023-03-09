import React from "react";
import { useUserAuth } from "../../context/UserAuthContext";
import ImageUpload from "../ImageUpload/ImageUpload";

const Home = () => {
  const { user } = useUserAuth();
  return (
    <>
      <div className="p-4 box mt-3 text-center">
        Welcome ! <br />
        {user && "Logged in using " + user.email}
      </div>
      <br/>
      <ImageUpload />
    </>
  );
};

export default Home;
