import { Link } from "react-router-dom";

// Presentational card for a single listing on the board.
export default function ListingCard({ listing }) {
  return (
    <Link to={`/listings/${listing.id}`} className="card">
      {listing.photo_url ? (
        <img className="card-img" src={listing.photo_url} alt={listing.title} />
      ) : (
        <div className="card-img placeholder">No photo</div>
      )}
      <div className="card-body">
        <span className={`badge ${listing.type}`}>{listing.type}</span>
        {listing.status === "resolved" && <span className="badge resolved"> resolved</span>}
        <h3>{listing.title}</h3>
        <p className="meta">📍 {listing.location} · {listing.category}</p>
        <p className="meta">{new Date(listing.created_at).toLocaleDateString()}</p>
      </div>
    </Link>
  );
}
