import React from "react";

function IncrementButton({ onClick }) {
    return (
        <div className="increment-button" onClick={onClick}>
        <button>+</button>
        </div>
    );
}

function DecrementButton({ onClick }) {
    return (
        <div className="decrement-button" onClick={onClick}>
        <button>-</button>
        </div>
    );
}

function Stat({ isConsumed }) {
    const statClassName = isConsumed ? "is-consumed" : "stat";
    return <div className={statClassName}></div>;
}

function StatsBar({ stats }) {
    return (
        <div className="stats-bar">
        {stats.map((isConsumed, index) => (
            <Stat key={index} isConsumed={isConsumed} />
        ))}
        </div>
    );
}

function IncrementableBar({
    attribute,
    stats,
    onIncrement,
    onDecrement,
    value,
    }) 
    {
    const handleIncrement = () => {
    onIncrement();
    };
    const handleDecrement = () => {
    onDecrement();
    };
    return (
        <div className="incrementable-bars">
            <div className="incrementable-bar-atribute">{attribute}</div>
            <StatsBar stats={stats} />
            <div className="incrementable-value">
                <div className="value-stat">{value}</div>
                    <IncrementButton onClick={handleIncrement} />
                    <DecrementButton onClick={handleDecrement} />
            </div>
        </div>
    );
}
export { IncrementableBar, StatsBar, Stat };
