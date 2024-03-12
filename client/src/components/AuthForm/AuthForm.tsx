import { FC, useState } from "react";

interface IAuthForm {
  type: "login" | "register";
  onSubmit: (username: string, password: string) => void;
}
const AuthForm: FC<IAuthForm> = ({ type, onSubmit }) => {
  const [details, setDetails] = useState({
    username: "",
    password: "",
  });

  return (
    <div>
      <input
        type="text"
        className="border-[1px] border-black"
        onChange={(e) => {
          setDetails({ ...details, username: e.target.value });
        }}
      />
      <input
        type="password"
        className="border-[1px] border-black"
        onChange={(e) => {
          setDetails({ ...details, password: e.target.value });
        }}
      />
      <button onClick={() => onSubmit(details.username, details.password)}>
        Sign {type === "login" ? "In" : "Up"}
      </button>
    </div>
  );
};

export default AuthForm;
