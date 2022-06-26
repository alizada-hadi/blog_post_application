// import { configureStore } from '@reduxjs/toolkit'
import { applyMiddleware, combineReducers, createStore } from 'redux'
import { composeWithDevTools } from 'redux-devtools-extension'
import { blogReducer } from './reducers/blogReducers'
import thunk from 'redux-thunk'

const initialState = {}
const reducer = combineReducers({
    blogList : blogReducer
})
const middleware = [thunk]

const store = createStore(
    reducer, 
    initialState, 
    composeWithDevTools(applyMiddleware(...middleware))
)

export default store