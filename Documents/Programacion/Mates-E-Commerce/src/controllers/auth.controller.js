import User from "../models/user.model.js";

export const register = async (req, res) => {
  const { username, email, password } = req.body;

  const newUser = new User({
    username,
    email,
    password,
  });

  const userSaved = await newUser.save();

  res.json({
    id: userSaved._id,
    username: userSaved.username,
    email: userSaved.email,
    createdAt: userSaved.createdAt,
    updatedAt: userSaved.updatedAt,
  });
};

export const login = (req, res) => {
  res.send("register");
};
