const st = {};

st.flap = document.querySelector('#flap');
st.toggle = document.querySelector('.toggle');

st.choice1 = document.querySelector('#choice1');
st.choice2 = document.querySelector('#choice2');

st.fileUpload = document.querySelector('#upload');
st.pastetextArea = document.querySelector('#textSpace');
st.contentPane = document.querySelector('#contentPane');


st.flap.addEventListener('transitionend', () => {

    if (st.choice1.checked) {
        st.contentPane.innerHTML = '<form action="upload.php" method="post" enctype="multipart/form-data"><div class="input-group-btn" style="border-radius: 2px 5px 5px 2px; border : 2px solid #2196F3 "><span class="fileUpload btn btn-success"><span class="w3-button" style="color: #ffffff ; background: #2196F3;" id="upload">Upload file</span><input type="file" class="upload up" id="fileToUpload" name="fileToUpload" onchange="readURL(this); required" /></span><span id="fileName" style="color :gray; padding: 8px; margin-top: 5px;  ">Upload Your File Here</span></div><!-- btn --><div class="input-container"><div id="contentPane" style = "text-align:center;"><br><button class="w3-button w3-light-grey w3-padding-large"  type="submit" name="uploadBtn">Generate</button></form></div> </div></div>';
//        st.contentPane.innerHTML = '<div class="input-container"><div id="contentPane"><form action="process.html" method="get"><input type="submit" class="submit w3-padding-16" style = "height: 55px;width: 155px; border-radius: 20px"></form></div> </div>';
//        st.fileUpload.style.visibility = "visible";
//        st.pastetextArea.style.visibility = "hidden";
        st.toggle.style.transform = 'rotateY(-15deg)';
        setTimeout(() => st.toggle.style.transform = '', 400);
    } else {
       
    st.contentPane.innerHTML = '<form action="upload.php" method="POST"><textarea placeholder=" Enter your Text Here . . " rows="4" cols="50" name="setText" id="setText" style="width:80%; padding:10px; height:50%; border-radius:20px; resize: inherit;" required></textarea><div class="input-container"><div id="contentPanel" style = "text-align:center;"><button class="w3-button w3-light-grey w3-padding-large" name="paste" type="submit">Generate</button></div></div></form>';
//        st.pastetextArea.style.visibility = "visible";
//        st.fileUpload.style.visibility = "hidden";
        st.toggle.style.transform = 'rotateY(15deg)';
        setTimeout(() => st.toggle.style.transform = '', 400);
    }

})

st.clickHandler = (e) => {

    if (e.target.tagName === 'LABEL') {
        setTimeout(() => {
            st.flap.children[0].textContent = e.target.textContent;
        }, 250);
    }
}

document.addEventListener('DOMContentLoaded', () => {
    st.flap.children[0].textContent = st.choice2.nextElementSibling.textContent;
});

document.addEventListener('click', (e) => st.clickHandler(e));