import client from "./client";

export const sendMessage = (data) => client.post("/api/messages", data);
export const getInbox = () => client.get("/api/messages/inbox");
