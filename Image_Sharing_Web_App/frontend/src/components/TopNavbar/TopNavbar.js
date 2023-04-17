import Container from 'react-bootstrap/Container';
import Navbar from 'react-bootstrap/Navbar';
import Nav from 'react-bootstrap/Nav';
import { Button } from "react-bootstrap";
import { useNavigate } from "react-router";
import { useUserAuth } from "../../context/UserAuthContext";
import { Icon } from '@iconify/react';
import LogoutIcon from '@mui/icons-material/Logout';


function TopNavbar() {

  const { logOut, user } = useUserAuth();
  const navigate = useNavigate();
  const handleLogout = async () => {
    try {
      await logOut();
      navigate("/login");
    } catch (error) {
      console.log(error.message);
    }
  };

  return (
    <>
      <Navbar bg="dark" variant="dark">
        <Container>
          <Navbar.Brand href="/">
            <Icon icon="mdi:instagram" className="mr-3 my-auto" color="#fbad50" width="35" height="35" />
            Decentragram - The Decentralized Image Sharing App</Navbar.Brand>
          <Nav className="d-grid gap-2 mx-3">
            <Nav.Link href="/users">Search Users</Nav.Link>
          </Nav>
        </Container>
        {user &&
          <div className="d-grid gap-2 mx-3">
            <Button variant="warning" onClick={handleLogout}>
              <LogoutIcon />
               Log out
            </Button>
          </div>
        }
      </Navbar>
    </>
  );
}

export default TopNavbar;