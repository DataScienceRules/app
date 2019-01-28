import React, from 'react';
import ReactDOM
import app from app;

var About = React.createClass({
    render: function () {
        return (
            <h1>About page</h1>
        )
    }
})

export default About;

function Square(props) {
    return(
        <button className="square" onClick={props.onClick}></button>
    )

}

