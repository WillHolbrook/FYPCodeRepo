import './App.css';
import Header from "./components/header";
import Footer from "./components/footer";
import Numbers from "./components/numbers";
import styled from "styled-components";

function createAlert() {
  alert('Helloo. You clicked me')
}

function ShowMessage(props) {
  if (props.toShow) {
    return <h2>My message</h2>
  } else {
    return <h2>Forbidden</h2>
  }

}

const pStyle = {
  fontSize: '2em',
  color: 'red'
}

const Paragraph = styled.p`
  font-size: 3em;
  color: green;
`;

function App() {
  return (
    <div className="App">
      <Header info="This is my message"/>
      <Header info="Header 2 Electric Booglaoo"/>
      <p style={pStyle}>main content</p>
      <Paragraph>New Styled</Paragraph>
      <Footer trademark="page by Will" myalert={createAlert}/>
      <ShowMessage toShow={false}/>
      <Numbers/>
    </div>
  );
}

export default App;
