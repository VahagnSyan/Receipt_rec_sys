import axios from "axios";

export const login = async (username: string, password: string) => {
  const response = await axios.post(
    "http://127.0.0.1:5000/login",
    {
      username,
      password,
    },
    {
      headers: {
        "Content-Type": "application/json",
      },
    }
  );
  if (response.data.success) {
    localStorage.setItem("token", "true");
  }
  return response.data;
};
export const register = async (username: string, password: string) => {
  const response = await axios.post(
    "http://127.0.0.1:5000/register",
    {
      username,
      password,
    },
    {
      headers: {
        "Content-Type": "application/json",
      },
    }
  );
  return response.data;
};
