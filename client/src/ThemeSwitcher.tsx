const ThemeSwitcher = () => {
  const toggleTheme = () => {
    document.documentElement.classList.add("light");
  };

  return (
    <button onClick={toggleTheme}>Switch to Light Theme</button>
  );
};

export default ThemeSwitcher;
