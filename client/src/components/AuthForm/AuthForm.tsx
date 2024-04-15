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
    <div className="h-[80vh] flex items-center justify-center ">
      <div className="flex flex-col gap-[20px] bg-[#26262C] p-[25px] rounded-xl">
        <h3 className="self-center text-[30px] text-white font-bold">{type.slice(0,1).toUpperCase()+ type.slice(1)}</h3>
        <input
          type="text"
          className="text-white bg-transparent border-[1px] border-white rounded-sm pl-[10px] pr-[20px] py-[10px] outline-none"
          onChange={(e) => {
            setDetails({ ...details, username: e.target.value });
          }}
          placeholder='Login'
        />
        <input
          type="password"
          className="text-white bg-transparent border-[1px] border-white rounded-sm pl-[10px] pr-[20px] py-[10px] outline-none"
          onChange={(e) => {
            setDetails({ ...details, password: e.target.value });
          }}
          placeholder='Password'

        />
        <button className="bg-white py-[15px] rounded-xl"  onClick={() => onSubmit(details.username, details.password)}>
          Sign {type === "login" ? "In" : "Up"}
        </button>
      </div>
    </div>
  );
};

export default AuthForm;
