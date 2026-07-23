// Single listing view. Shows full details, a contact form for logged-in users
// who don't own the listing, and owner controls (edit / resolve / delete).
import { useState, useEffect } from "react";
import { useParams, useNavigate, Link } from "react-router-dom";
import { getListing, deleteListing, resolveListing } from "../api/listings";
import { sendMessage } from "../api/messages";
import { useAuth } from "../context/AuthContext";

export default function ListingDetail() {
  const { id } = useParams();
  const navigate = useNavigate();
  const { user } = useAuth();

  const [listing, setListing] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState("");

  const [body, setBody] = useState("");
  const [msgState, setMsgState] = useState({ sending: false, ok: "", err: "" });

  useEffect(() => {
    getListing(id)
      .then((res) => setListing(res.data))
      .catch(() => setError("Listing not found"))
      .finally(() => setLoading(false));
  }, [id]);

  const isowner = user && listing && user.id === listing.user_id;

  const onResolve = async () => {
    await resolveListing(id);
    setListing({ ...listing, status: "resolved" });
  };

  const onDelete = async () => {
    if (!window.confirm("Delete this listing? This cannot be undone.")) return;
    await deleteListing(id);
    navigate("/");
  };

  const onContact = async (e) => {
    e.preventDefault();
    setMsgState({ sending: true, ok: "", err: "" });
    try {
      await sendMessage({ listing_id: Number(id), body });
      setBody("");
      setMsgState({ sending: false, ok: "Message sent to the poster.", err: "" });
    } catch (err) {
      setMsgState({ sending: false, ok: "", err: err.response?.data?.detail || "Could not send" });
    }
  };

  if (loading) return <div className="spinner">Loading…</div>;
  if (error) return <div className="muted-box">{error}</div>;

  return (
    <div style={{ maxWidth: 640, margin: "24px auto" }}>
      <Link to="/" className="meta">← Back to board</Link>

      {listing.photo_url ? (
        <img className="detail-img" src={listing.photo_url} alt={listing.title} style={{ marginTop: 12 }} />
      ) : (
        <div className="detail-img card-img placeholder" style={{ marginTop: 12 }}>No photo</div>
      )}

      <div className="row" style={{ marginTop: 14 }}>
        <span className={`badge ${listing.type}`}>{listing.type}</span>
        {listing.status === "resolved" && <span className="badge resolved">resolved</span>}
      </div>

      <h1 style={{ margin: "10px 0 4px" }}>{listing.title}</h1>
      <p className="meta">📍 {listing.location} · {listing.category} · posted by {listing.owner_name}</p>
      <p className="meta">{new Date(listing.created_at).toLocaleString()}</p>
      <p style={{ marginTop: 12 }}>{listing.description}</p>

      {isowner && (
        <div className="row" style={{ marginTop: 16 }}>
          <Link to={`/listings/${id}/edit`} className="btn btn-sm btn-outline">Edit</Link>
          {listing.status === "active" && (
            <button className="btn btn-sm" onClick={onResolve}>Mark resolved</button>
          )}
          <button className="btn btn-sm btn-danger" onClick={onDelete}>Delete</button>
        </div>
      )}

      {!isowner && (
        <div className="form" style={{ margin: "24px 0 0", maxWidth: "none" }}>
          <h2 style={{ fontSize: 18 }}>Contact the poster</h2>
          {!user && <p className="meta">Please <Link to="/login">log in</Link> to send a message.</p>}
          {user && (
            <form onSubmit={onContact}>
              {msgState.ok && <div className="form-ok">{msgState.ok}</div>}
              {msgState.err && <div className="form-error">{msgState.err}</div>}
              <div className="field">
                <textarea
                  value={body}
                  onChange={(e) => setBody(e.target.value)}
                  placeholder="Write a message…"
                  required
                />
              </div>
              <button className="btn" disabled={msgState.sending || !body.trim()}>
                {msgState.sending ? "Sending…" : "Send message"}
              </button>
            </form>
          )}
        </div>
      )}
    </div>
  );
}
