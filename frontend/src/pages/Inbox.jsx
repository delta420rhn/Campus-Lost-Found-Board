// Messages received on the logged-in user's listings.
import { useState, useEffect } from "react";
import { getInbox } from "../api/messages";
import { Link } from "react-router-dom";

export default function Inbox() {
  const [messages, setMessages] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    getInbox()
      .then((res) => setMessages(res.data))
      .finally(() => setLoading(false));
  }, []);

  return (
    <>
      <div className="page-head"><h1>Inbox</h1></div>
      {loading && <div className="spinner">Loading…</div>}
      {!loading && messages.length === 0 && (
        <div className="muted-box">No messages yet.</div>
      )}
      {!loading && messages.map((m) => (
        <div className="card" key={m.id} style={{ marginBottom: 12 }}>
          <div className="card-body">
            <p className="meta">
              From <strong>{m.sender_name}</strong> about{" "}
              <Link to={`/listings/${m.listing_id}`}>{m.listing_title}</Link>
            </p>
            <p>{m.body}</p>
            <p className="meta">{new Date(m.sent_at).toLocaleString()}</p>
          </div>
        </div>
      ))}
    </>
  );
}
