import React, {useEffect, Fragment} from 'react'
import { useDispatch, useSelector } from 'react-redux'
import { allBlogs } from '../actions/blogActions'
import Loader from '../components/Loader'
import Message from '../components/Message'
import Blog from '../components/Blog'


function Home() {
    const dispatch = useDispatch()
    const blogList = useSelector(state => state.blogList)
    const {blogs, loading, error} = blogList
    useEffect(() => {
        dispatch(allBlogs())
    }, [dispatch])

  return (
    <div className='container mx-auto'>
       <div className="flex mt-5">
            <div className="flex-auto"></div>
            <div className="flex-auto w-64">
                <h1>All Posts</h1>
                {
                    loading ? <Loader />
                    : error ? <Message message={error} />
                    :
                    
                    blogs.map(blog => (
                        <Blog key={blog.id} blog={blog} />
                    ))
                }    
            </div>
            <div className="flex-auto"></div>
       </div>
    </div>
  )
}

export default Home