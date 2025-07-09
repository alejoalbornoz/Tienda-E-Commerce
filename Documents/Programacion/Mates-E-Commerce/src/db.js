import mongoose from "mongoose";

export const connectDB = async () => {
  try {
    await mongoose.connect("mongodb://127.0.0.1:27017/mates-e-commerce");
    console.log("MongoDB is connected");
  } catch (error) {
    console.log("Error connecting MongoDB", error);
  }
};
