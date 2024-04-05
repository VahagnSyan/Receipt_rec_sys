import { useNavigate } from "react-router-dom";
import { register } from "../../../services/authentication";
import AuthForm from "../../AuthForm/AuthForm";

const SignUp = () => {
  const navigate = useNavigate();

  const handleRegister = async (username: string, password: string) => {
    await register(username, password).then((response) => {
      if (response.success) {
        navigate("/sign-in");
        navigate(0);
      }
    });
  };
  return (
    <div>
      <AuthForm type="register" onSubmit={handleRegister} />
    </div>
  );
};

export default SignUp;
