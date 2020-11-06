<template>
  <div class="container">
    <div style="width:95%; margin:0 auto; display:block;height:420px;">
      <span style="display:inline-block;width:45%;height:400px;">
        <textarea v-model="message" placeholder="add multiple lines"></textarea>
      </span>
      <span class="button_container">
        <InkButton/>
        <button v-on:click="send">言葉を色付ける</button>
      </span>
    </div>
    <div id="result" class="result_container">
      <div id="result_color" class="result_color">{{ message_color }}</div>
      <div id="result_message">{{ message }}</div>
    </div>
  </div>
</template>

<script>
export default {
  data () {
    return {
      message: '',
      message_color: ''
    }
  },
  methods: {
    async send () {
      // location.href = '/output'
      /*
      const request = new XMLHttpRequest()
      request.withCredentials = true
      const url = 'http://ec2-54-88-164-239.compute-1.amazonaws.com:8080/?sentence=' + this.message
      request.withCredentials = true
      request.open('GET', url, true)
      request.responseType = 'json'
      request.onload = function () {
        const data = this.response
        console.log(data)
        this.$set(this.message_color, 'value', data.ink)
      }

      request.send()
      document.getElementById('result').style.color = 'red'
      */
      if (this.message === '') {
        return
      }
      const url = 'http://ec2-54-88-164-239.compute-1.amazonaws.com:8080/?sentence=' + this.message
      const responce = await this.$axios.$get(url)
      console.log(responce)
      this.message_color = responce.ink + 'の色'
      document.getElementById('result_message').style.color = responce.colorcode
      document.getElementById('result_color').style.background = responce.colorcode
    }
  }
}
</script>

<style>
html{
  background-image:url("~static/background_image.png");
  background-size:cover;
  background-color: rgba(255,255,255,0.4);
  background-blend-mode: lighten;
}
.container {
  width:80%;
  margin: 0 auto;
  padding-top:10vh;
  padding-bottom:10vh;
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  align-items: center;
  text-align: center;
  background-color: white;
}

textarea{
  width:100%;
  height:100%;
}
.button_container{
  display:inline-block;
  padding:20px;
  width:45%;
}
button {
  /*
  border:0;
  background:none;
  */
  border:0;
  background:#abece9;
  color:rgb(17, 65, 71);
  border-radius: 10px;
  display:block;
  margin: 0 auto;
}
.result_container{
  display:block;
  width:80%;
  margin:0 auto;
}
.result_color{
  height:40px;
  background: none;
  color:white;
}

</style>
