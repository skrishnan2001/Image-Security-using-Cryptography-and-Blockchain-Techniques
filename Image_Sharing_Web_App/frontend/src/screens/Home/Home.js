import React from "react";
import { useUserAuth } from "../../context/UserAuthContext";
import SharedWith from "../Users/SharedWith";

const Home = () => {
  const { user } = useUserAuth();
  return (
    <>
      <div className="p-4 box mt-3 text-center h5 bg-light text-dark">
        Welcome! <br />
        {user && "Logged in using " + user.email}
      </div>
      <br />
      {/* <ImageUpload /> */}

      <SharedWith email={user.email}/>
    </>
  );
};

export default Home;
