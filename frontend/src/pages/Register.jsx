import { useState } from "react";
import { useNavigate, Link } from "react-router-dom";
import { useAuth } from "../context/AuthContext";

export default function Register() {
  const { register } = useAuth();
  const navigate = useNavigate();
  const [form, setForm] = useState({ name: "", email: "", password: "" });
  const [errors, setErrors] = useState({});
  const [apiError, setApiError] = useState("");
  const [loading, setLoading] = useState(false);

  const change = (e) => setForm({ ...form, [e.target.name]: e.target.value });

  const validate = () => {
    const err = {};
    if (form.name.trim().length < 2) err.name = "Name is too short";
    if (!/^\S+@\S+\.\S+$/.test(form.email)) err.email = "Enter a valid email";
    if (form.password.length < 6) err.password = "Password must be at least 6 characters";
    setErrors(err);
    return Object.keys(err).length === 0;
  };

  const submit = async (e) => {
    e.preventDefault();
    setApiError("");
    if (!validate()) return;
    setLoading(true);
    try {
      await register(form.name, form.email, form.password);
      navigate("/");
    } catch (err) {
      setApiError(err.response?.data?.detail || "Registration failed");
    } finally {
      setLoading(false);
    }
  };

  return (
    <form className="form" onSubmit={submit}>
      <h2>Create an account</h2>
      {apiError && <div className="form-error">{apiError}</div>}
      <div className="field">
        <label>Name</label>
        <input name="name" value={form.name} onChange={change} />
        {errors.name && <div className="err">{errors.name}</div>}
      </div>
      <div className="field">
        <label>University email</label>
        <input name="email" value={form.email} onChange={change} />
        {errors.email && <div className="err">{errors.email}</div>}
      </div>
      <div className="field">
        <label>Password</label>
        <input type="password" name="password" value={form.password} onChange={change} />
        {errors.password && <div className="err">{errors.password}</div>}
      </div>
      <button className="btn" disabled={loading}>{loading ? "Creating…" : "Sign up"}</button>
      <p className="meta" style={{ marginTop: 14 }}>
        Already have an account? <Link to="/login">Log in</Link>
      </p>
    </form>
  );
}
