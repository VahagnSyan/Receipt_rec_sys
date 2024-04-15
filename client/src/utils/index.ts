export const getCurrentUserId = () => {
  return localStorage.getItem("id")!;
};
