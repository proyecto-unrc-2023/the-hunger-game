import React from "react";
import { render } from "@testing-library/react";
import {Stat, StatsBar, IncrementableBar} from "../components/IncrementableBar.jsx";

describe ("IncrementableBar component", () => {

  it('should render a stat with the "consumed" class when isConsumed is true', () => {
    const { container } = render(<Stat isConsumed = {true} />);
    const stat = container.querySelector(".is-consumed");
    expect(stat).toBeInTheDocument();
  });

  it('should render a stat with the "unconsumed" class when isConsumed is false', () => {
    const { container } = render(<Stat isConsumed = {false} />);
    const stat = container.querySelector(".stat");
    expect(stat).toBeInTheDocument();
  });

  it('should render a statBar without a consumed stat', () => {
    const { container } = render(<StatsBar stats = {Array(10).fill(false)} />);
    const statBar = container.querySelector(".stats-bar");
    const statBarConsumed = container.querySelector(".is-consumed");
    const statBarUnconsumed = container.querySelector(".stat");
    expect(statBar).toBeInTheDocument();
    expect(statBarUnconsumed).toBeInTheDocument();
    expect(statBarConsumed).not.toBeInTheDocument();
  });

  it('should render a statBar without a unconsumed stat', () => {
    const { container } = render(<StatsBar stats = {Array(10).fill(true)} />);
    const statBar = container.querySelector(".stats-bar");
    const statBarConsumed = container.querySelector(".is-consumed");
    const statBarUnconsumed = container.querySelector(".stat");
    expect(statBar).toBeInTheDocument();
    expect(statBarConsumed).toBeInTheDocument();
    expect(statBarUnconsumed).not.toBeInTheDocument();
  });

  it('should render a statBar with some consumed stat', () => {
    const { container } = render(<StatsBar stats = {[true, false]} />);
    const statBar = container.querySelector(".stats-bar");
    const statBarConsumed = container.querySelector(".is-consumed");
    const statBarUnconsumed = container.querySelector(".stat");
    expect(statBar).toBeInTheDocument();
    expect(statBarConsumed).toBeInTheDocument();
    expect(statBarUnconsumed).toBeInTheDocument();
  });

  it('should render a incrementableBar', () => {
    const { container } = render(<IncrementableBar stats = {Array(10).fill(false)}  />);
    const statBar = container.querySelector(".stats-bar");
    const incrementButton = container.querySelector(".increment-button");
    const decrementButton = container.querySelector(".decrement-button");
    expect(statBar).toBeInTheDocument();
    expect(incrementButton).toBeInTheDocument();
    expect(decrementButton).toBeInTheDocument();
  });

})