import { useNavigate } from "react-router-dom";
import { login } from "../../../services/authentication";
import AuthForm from "../../AuthForm/AuthForm";

const SignIn = () => {
  const navigate = useNavigate();
  const handleLogin = async (username: string, password: string) => {
    await login(username, password).then((response) => {
      if (response.success) {
        navigate("/");
      }
    });
  };
  return (
    <div>
      <AuthForm type="login" onSubmit={handleLogin} />
    </div>
  );
};

export default SignIn;
