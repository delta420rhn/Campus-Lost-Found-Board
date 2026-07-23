// All listing-related API calls grouped together.
import client from "./client";

export const getListings = (params) => client.get("/api/listings", { params });
export const getListing = (id) => client.get(`/api/listings/${id}`);
export const getMyListings = () => client.get("/api/listings/mine");
export const createListing = (data) => client.post("/api/listings", data);
export const updateListing = (id, data) => client.put(`/api/listings/${id}`, data);
export const deleteListing = (id) => client.delete(`/api/listings/${id}`);
export const resolveListing = (id) => client.patch(`/api/listings/${id}/resolve`);
