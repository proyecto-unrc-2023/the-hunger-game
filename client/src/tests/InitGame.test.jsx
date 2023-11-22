import React from "react";
import { render } from "@testing-library/react";
import InitGame from "../components/InitGame.jsx";

describe ("Board component", () => {

  it("should render a game init", () => {
    const { container } = render(<InitGame onViewChange={"init"} isLoggedIn={true} />);
    const header = container.querySelector(".header");
    const video = container.querySelector(".video");
    const buttonPlayGame = container.querySelectorAll(".button-play-game");
    const buttonLoggedOut = container.querySelector(".logout");
    const footer = container.querySelector(".footer");
    expect(header).toBeInTheDocument();
    expect(video).toBeInTheDocument();
    expect(buttonPlayGame).toHaveLength(3);
    expect(buttonLoggedOut).toBeInTheDocument();
    expect(footer).toBeInTheDocument();
  });

});