// INSTALLATION 

// Note: this is basically replacing form textarea

// Terminal command
npm install react-quill --save

import React, { useState } from 'react';
import ReactQuill from 'react-quill';
import 'react-quill/dist/quill.snow.css'; // Optional: Include Quill styles

const SimpleEditor = () => {
  const [content, setContent] = useState('');

  return (
    <div>
    	<ReactQuill
    		required 
            id='comment' 
            name='comment'
            ref={commentContent}
            placeholder='Add a comment'
            theme="snow"
    	/>
	</div>
  );
};

export default SimpleEditor;


// RENDER CONTENTS

// Terminal command:
npm install dompurify

import DOMPurify from 'dompurify';

const Editor = () => {
  const [content, setContent] = useState('');

  const handleContentChange = (value) => {
    setContent(value); // Get the content from ReactQuill
  };

  const sanitizedContent = DOMPurify.sanitize(content);  // Sanitize the content

  return (
    <div>
      <ReactQuill 
        value={content}
        onChange={handleContentChange} 
        theme="snow" 
      />
      
      <div style={{ marginTop: '20px' }}>
        <h4>Preview:</h4>
        <div dangerouslySetInnerHTML={{ __html: sanitizedContent }} />
      </div>
    </div>
  );
};

export default Editor;

