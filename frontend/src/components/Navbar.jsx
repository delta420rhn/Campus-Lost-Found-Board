import { NavLink, useNavigate } from "react-router-dom";
import { useAuth } from "../context/AuthContext";

export default function Navbar() {
  const { user, logout } = useAuth();
  const navigate = useNavigate();

  const onLogout = () => {
    logout();
    navigate("/");
  };

  return (
    <nav className="nav">
      <div className="container nav-inner">
        <NavLink to="/" className="nav-brand">Campus Lost &amp; Found</NavLink>
        <NavLink to="/" end>Board</NavLink>
        {user && <NavLink to="/post">Post</NavLink>}
        {user && <NavLink to="/inbox">Inbox</NavLink>}
        {user && <NavLink to="/profile">My Listings</NavLink>}
        <span className="nav-spacer" />
        {user ? (
          <>
            <span className="meta">Hi, {user.name.split(" ")[0]}</span>
            <button className="btn btn-sm btn-outline" onClick={onLogout}>Logout</button>
          </>
        ) : (
          <>
            <NavLink to="/login">Login</NavLink>
            <NavLink to="/register" className="btn btn-sm">Sign up</NavLink>
          </>
        )}
      </div>
    </nav>
  );
}
