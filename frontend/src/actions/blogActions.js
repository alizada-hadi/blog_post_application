import { 
    BLOG_LIST_REQUEST, 
    BLOG_LIST_SUCCESS, 
    BLOG_LIST_FAIL
 } from '../constants/blogConstants'

 import axios from 'axios'


 export const allBlogs = () => async dispatch => {
    try{
        dispatch({
            type : BLOG_LIST_REQUEST
        })

        const {data} = await axios.get("/api/articles/")
        dispatch({
            type : BLOG_LIST_SUCCESS, 
            payload : data
        })
    }catch(error){
        dispatch({
            BLOG_LIST_FAIL, 
            payload : "error accured"
        })
    }
 }