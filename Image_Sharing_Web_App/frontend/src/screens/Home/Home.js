import React from "react";
import { useUserAuth } from "../../context/UserAuthContext";
import ImageUpload from "../ImageUpload/ImageUpload";
import Users from "../Users/Users";

const Home = () => {
  const { user } = useUserAuth();
  return (
    <>
      <div className="p-4 box mt-3 text-center h5 bg-light text-dark">
        Welcome! <br />
        {user && "Logged in using " + user.email}
      </div>
      <br />
      <ImageUpload />

      <Users />
    </>
  );
};

export default Home;
