import React from 'react'

function Message({message, type}) {
  return (
    <div className="p-4 mb-4 text-sm text-blue-700 bg-blue-100 rounded-lg dark:bg-blue-200 dark:text-blue-800" role="alert">
        <span className="font-medium">{message}</span> 
    </div>
  )
}

export default Message