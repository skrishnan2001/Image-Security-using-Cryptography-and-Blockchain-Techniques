import Container from 'react-bootstrap/Container';
import Navbar from 'react-bootstrap/Navbar';
import { Button } from "react-bootstrap";
import { useNavigate } from "react-router";
import { useUserAuth } from "../../context/UserAuthContext";
import { Icon } from '@iconify/react';


function TopNavbar() {

  const { logOut, user } = useUserAuth();
  const navigate = useNavigate();
  const handleLogout = async () => {
    try {
      await logOut();
      navigate("/");
    } catch (error) {
      console.log(error.message);
    }
  };

  return (
    <>
      <Navbar bg="dark" variant="dark">
        <Container>
          <Navbar.Brand href="/home">
          <Icon icon="mdi:instagram" color="#e95950" /> Decentragram - The Decentralized Image Sharing App</Navbar.Brand>
        </Container>
        {user &&
          <div className="d-grid gap-2 mx-3">
            <Button variant="warning" onClick={handleLogout}>
              Log out
            </Button>
          </div>
        }
      </Navbar>
    </>
  );
}

export default TopNavbar;