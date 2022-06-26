import { Provider } from 'react-redux'
import store from './store';
function App() {
  return (
    <Provider store={store}>
      <div className="">
        <h1 className="text-5xl">Hello World</h1>
      </div>
    </Provider>
  );
}

export default App;
