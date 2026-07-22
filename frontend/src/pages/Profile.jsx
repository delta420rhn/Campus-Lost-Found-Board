// Shows all listings created by the logged-in user, including resolved ones.
import { useState, useEffect } from "react";
import { getMyListings } from "../api/listings";
import ListingCard from "../components/ListingCard";
import { Link } from "react-router-dom";

export default function Profile() {
  const [listings, setListings] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    getMyListings()
      .then((res) => setListings(res.data))
      .finally(() => setLoading(false));
  }, []);

  return (
    <>
      <div className="page-head">
        <h1>My Listings</h1>
        <Link to="/post" className="btn btn-sm">Post new</Link>
      </div>
      {loading && <div className="spinner">Loading…</div>}
      {!loading && listings.length === 0 && (
        <div className="muted-box">You have not posted anything yet.</div>
      )}
      {!loading && listings.length > 0 && (
        <div className="grid">
          {listings.map((l) => <ListingCard key={l.id} listing={l} />)}
        </div>
      )}
    </>
  );
}
