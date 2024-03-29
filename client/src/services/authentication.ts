import axios from "axios";
import { IProduct } from "../types";

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

export const getReceiptProducts = async (id: string, image: File) => {
  const formData = new FormData();
  formData.append("id", id);
  formData.append("images", image);
  const response = await axios.post(
    "http://127.0.0.1:5000/process-images",
    formData
  );

  return response.data.results;
};

export const addProducts = async (id: string, products: IProduct[]) => {
  const response = await axios.post("http://127.0.0.1:5000/add", {
    id,
    products,
  });

  return response.data;
};
