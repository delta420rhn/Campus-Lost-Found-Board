// Main board page: lists all active listings with keyword search and filters.
// Guests can view this page. Demonstrates useState/useEffect, loading state,
// and firing the GET /api/listings request.
import { useState, useEffect } from "react";
import { getListings } from "../api/listings";
import ListingCard from "../components/ListingCard";

const CATEGORIES = ["electronics", "documents", "accessories", "clothing", "other"];
const LOCATIONS = ["library", "gym", "cafeteria", "lecture-hall", "parking", "other"];

export default function Board() {
  const [listings, setListings] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState("");

  // Filter inputs kept in state so the UI is controlled.
  const [search, setSearch] = useState("");
  const [category, setCategory] = useState("");
  const [location, setLocation] = useState("");

  // Fetch listings whenever a filter changes.
  useEffect(() => {
    let active = true;
    const fetchListings = async () => {
      setLoading(true);
      setError("");
      try {
        const params = {};
        if (search) params.search = search;
        if (category) params.category = category;
        if (location) params.location = location;
        const res = await getListings(params);
        if (active) setListings(res.data);
      } catch (e) {
        if (active) setError("Could not load listings. Is the API running?");
      } finally {
        if (active) setLoading(false);
      }
    };
    // Debounce so we don't fire a request on every keystroke.
    const t = setTimeout(fetchListings, 300);
    return () => { active = false; clearTimeout(t); };
  }, [search, category, location]);

  return (
    <>
      <div className="page-head">
        <h1>Lost &amp; Found Board</h1>
      </div>

      <div className="toolbar">
        <input
          placeholder="Search by keyword…"
          value={search}
          onChange={(e) => setSearch(e.target.value)}
        />
        <select value={category} onChange={(e) => setCategory(e.target.value)}>
          <option value="">All categories</option>
          {CATEGORIES.map((c) => <option key={c} value={c}>{c}</option>)}
        </select>
        <select value={location} onChange={(e) => setLocation(e.target.value)}>
          <option value="">All locations</option>
          {LOCATIONS.map((l) => <option key={l} value={l}>{l}</option>)}
        </select>
      </div>

      {loading && <div className="spinner">Loading listings…</div>}
      {error && <div className="form-error">{error}</div>}
      {!loading && !error && listings.length === 0 && (
        <div className="muted-box">No results found.</div>
      )}

      {!loading && !error && listings.length > 0 && (
        <div className="grid">
          {listings.map((l) => <ListingCard key={l.id} listing={l} />)}
        </div>
      )}
    </>
  );
}
