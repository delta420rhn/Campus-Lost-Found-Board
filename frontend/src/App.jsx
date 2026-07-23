// Top-level component: sets up the navbar and all client-side routes.
import { Routes, Route } from "react-router-dom";
import Navbar from "./components/Navbar";
import ProtectedRoute from "./components/ProtectedRoute";
import Board from "./pages/Board";
import ListingDetail from "./pages/ListingDetail";
import PostListing from "./pages/PostListing";
import Login from "./pages/Login";
import Register from "./pages/Register";
import Profile from "./pages/Profile";
import Inbox from "./pages/Inbox";

export default function App() {
  return (
    <>
      <Navbar />
      <main className="container">
        <Routes>
          <Route path="/" element={<Board />} />
          <Route path="/listings/:id" element={<ListingDetail />} />
          <Route path="/login" element={<Login />} />
          <Route path="/register" element={<Register />} />
          <Route
            path="/post"
            element={<ProtectedRoute><PostListing /></ProtectedRoute>}
          />
          <Route
            path="/listings/:id/edit"
            element={<ProtectedRoute><PostListing /></ProtectedRoute>}
          />
          <Route
            path="/profile"
            element={<ProtectedRoute><Profile /></ProtectedRoute>}
          />
          <Route
            path="/inbox"
            element={<ProtectedRoute><Inbox /></ProtectedRoute>}
          />
        </Routes>
      </main>
    </>
  );
}
