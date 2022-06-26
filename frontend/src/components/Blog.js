import React from 'react'

function Blog({blog}) {
  return (
    <div className='bg-white py-4'>
        <div className="flex bg-white items-center space-x-4">
            <img className="w-10 h-10 ml-5 rounded-full" src="https://png.pngtree.com/png-vector/20190704/ourlarge/pngtree-businessman-user-avatar-free-vector-png-image_1538405.jpg" alt="" />
            <div className=" font-medium dark:text-white">
                <div>{blog.author}</div>
                <div className="text-sm text-gray-500 dark:text-gray-400">Joined in August 2014</div>
            </div>
        </div>
        <h1 className='mt-3 ml-5 text-2xl'>{blog.title}</h1>
        <p className='ml-5'>{blog.body}</p>

    </div>
  )
}

export default Blog