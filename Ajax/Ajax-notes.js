<script type="text/javascript">
        // SEND FORM USING AJAX:
        const tweetForm = document.querySelector('#tweet-container')
        const tweetContainer = document.querySelector('.tweet-container')
        tweetForm.addEventListener('submit', function(event) {
            event.preventDefault()
            const tweetForm = event.target
            const newTweet = new FormData(tweetForm)
            const method = tweetForm.getAttribute('method')
            const url = tweetForm.getAttribute('action')
            const responseType = 'json'
            const xhr = new XMLHttpRequest()

            xhr.responseType = responseType
            xhr.open(method, url)
            xhr.setRequestHeader('HTTP_X_REQUESTED_WITH', 'XMLHttpRequest')
            xhr.setRequestHeader('X-Requested-With', 'XMLHttpRequest')
            xhr.onload = function() {
                const jsonResponse = xhr.response
                let formatTweet = `<div>
                                        <p>ID ${jsonResponse.id}</p>
                                        <h3>${jsonResponse.title}</h3>
                                        <p>${jsonResponse.content}</p>
                                    </div>`
                tweetContainer.innerHTML = formatTweet + tweetContainer.innerHTML            
            }
            xhr.send(newTweet)
        })

        //RENDER OUT TWEETS FROM DATA BASE
        function loadTweets(){
            console.log('reloaded')
            const xhr = new XMLHttpRequest()
            const method = 'GET'
            const url = '/tweets'
            const responseType = 'json'

            xhr.responseType = responseType
            xhr.open(method, url)
            xhr.onload = function(){
                let tweetWrapper = ''
                const tweets = xhr.response
                let new_tweets = [...tweets.tweet_list]
                new_tweets.forEach(function(item){
                    tweetWrapper += `
                                    <div class="tweet-wrapper">
                                        <p>ID - ${item.id}</p>
                                        <p>Content - ${item.content}</p>
                                    </div>
                                    `
                })
                tweetsContainer.innerHTML = tweetWrapper
            }
            xhr.send()
        }
        loadTweets()


    </script>