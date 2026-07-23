// Create a new listing, or edit an existing one when an :id param is present.
// This is the main "feature" for the viva: user fills the form, submits, and a
// POST /api/listings request is fired.
import { useState, useEffect } from "react";
import { useNavigate, useParams } from "react-router-dom";
import { createListing, updateListing, getListing } from "../api/listings";

const CATEGORIES = ["electronics", "documents", "accessories", "clothing", "other"];
const LOCATIONS = ["library", "gym", "cafeteria", "lecture-hall", "parking", "other"];

const EMPTY = { type: "lost", title: "", description: "", category: "", location: "", photo_url: "" };

export default function PostListing() {
  const { id } = useParams();          // present when editing
  const isEdit = Boolean(id);
  const navigate = useNavigate();

  const [form, setForm] = useState(EMPTY);
  const [errors, setErrors] = useState({});
  const [apiError, setApiError] = useState("");
  const [loading, setLoading] = useState(false);
  const [loadingListing, setLoadingListing] = useState(isEdit);

  // When editing, load the current values into the form.
  useEffect(() => {
    if (!isEdit) return;
    getListing(id)
      .then((res) => {
        const l = res.data;
        setForm({
          type: l.type, title: l.title, description: l.description,
          category: l.category, location: l.location, photo_url: l.photo_url || "",
        });
      })
      .catch(() => setApiError("Could not load the listing to edit"))
      .finally(() => setLoadingListing(false));
  }, [id, isEdit]);

  const change = (e) => setForm({ ...form, [e.target.name]: e.target.value });

  const validate = () => {
    const err = {};
    if (form.title.trim().length < 2) err.title = "Title is required";
    if (form.description.trim().length < 2) err.description = "Description is required";
    if (!form.category) err.category = "Pick a category";
    if (!form.location) err.location = "Pick a location";
    setErrors(err);
    return Object.keys(err).length === 0;
  };

  const submit = async (e) => {
    e.preventDefault();
    setApiError("");
    if (!validate()) return;
    setLoading(true);
    try {
      // Drop empty photo_url so we send null rather than "".
      const payload = { ...form, photo_url: form.photo_url.trim() || null };
      if (isEdit) {
        await updateListing(id, payload);
        navigate(`/listings/${id}`);
      } else {
        const res = await createListing(payload);
        navigate(`/listings/${res.data.id}`);
      }
    } catch (err) {
      setApiError(err.response?.data?.detail || "Something went wrong");
    } finally {
      setLoading(false);
    }
  };

  if (loadingListing) return <div className="spinner">Loading…</div>;

  return (
    <form className="form" onSubmit={submit}>
      <h2>{isEdit ? "Edit listing" : "Post a listing"}</h2>
      {apiError && <div className="form-error">{apiError}</div>}

      <div className="field">
        <label>Type</label>
        <select name="type" value={form.type} onChange={change}>
          <option value="lost">Lost</option>
          <option value="found">Found</option>
        </select>
      </div>
      <div className="field">
        <label>Title</label>
        <input name="title" value={form.title} onChange={change} placeholder="e.g. Black car keys" />
        {errors.title && <div className="err">{errors.title}</div>}
      </div>
      <div className="field">
        <label>Description</label>
        <textarea name="description" value={form.description} onChange={change} />
        {errors.description && <div className="err">{errors.description}</div>}
      </div>
      <div className="field">
        <label>Category</label>
        <select name="category" value={form.category} onChange={change}>
          <option value="">Select…</option>
          {CATEGORIES.map((c) => <option key={c} value={c}>{c}</option>)}
        </select>
        {errors.category && <div className="err">{errors.category}</div>}
      </div>
      <div className="field">
        <label>Campus location</label>
        <select name="location" value={form.location} onChange={change}>
          <option value="">Select…</option>
          {LOCATIONS.map((l) => <option key={l} value={l}>{l}</option>)}
        </select>
        {errors.location && <div className="err">{errors.location}</div>}
      </div>
      <div className="field">
        <label>Photo URL (optional)</label>
        <input name="photo_url" value={form.photo_url} onChange={change} placeholder="https://…" />
      </div>

      <button className="btn" disabled={loading}>
        {loading ? "Saving…" : isEdit ? "Save changes" : "Post listing"}
      </button>
    </form>
  );
}
