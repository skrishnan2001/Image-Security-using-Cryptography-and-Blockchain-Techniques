import { Container, Row, Col } from "react-bootstrap";
import { Routes, Route } from "react-router-dom";
import "./App.css";
import Home from "./screens/Home/Home";
import Login from "./screens/Authentication/Login";
import Signup from "./screens/Authentication/Signup";
import ProtectedRoute from "./screens/ProtectedRoute";
import { UserAuthContextProvider } from "./context/UserAuthContext";
import TopNavbar from "./components/TopNavbar/TopNavbar"
import AllUsers from "./screens/Users/AllUsers";


function App() {
  return (
    <>
      <UserAuthContextProvider>
        <TopNavbar />
        <Container style={{ width: "800px" }}>
          <Row>
            <Col>
              <Routes>
                <Route path="/login" element={<Login />} />
                <Route path="/signup" element={<Signup />} />
                <Route
                  path="/"
                  element={
                    <ProtectedRoute>
                      <Home />
                    </ProtectedRoute>
                  }
                />
                <Route
                  path="/users"
                  element={
                    <ProtectedRoute>
                      <AllUsers />
                    </ProtectedRoute>
                  }
                />
              </Routes>
            </Col>
          </Row>
        </Container>
      </UserAuthContextProvider>
    </>
  );
}

export default App;
