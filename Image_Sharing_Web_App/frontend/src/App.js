import { Container, Row, Col } from "react-bootstrap";
import { Routes, Route } from "react-router-dom";
import "./App.css";
import Home from "./screens/Home";
import Login from "./screens/Authentication/Login";
import Signup from "./screens/Authentication/Signup";
import ProtectedRoute from "./screens/ProtectedRoute";
import { UserAuthContextProvider } from "./context/UserAuthContext";
import TopNavbar from "./components/TopNavbar"


function App() {
  return (
    <>
    <TopNavbar />
    <Container style={{ width: "400px" }}>
      <Row>
        <Col>
          <UserAuthContextProvider>
            <Routes>
              <Route
                path="/home"
                element={
                  <ProtectedRoute>
                    <Home />
                  </ProtectedRoute>
                }
              />
              <Route path="/" element={<Login />} />
              <Route path="/signup" element={<Signup />} />
            </Routes>
          </UserAuthContextProvider>
        </Col>
      </Row>
    </Container>
    </>
  );
}

export default App;
