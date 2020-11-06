<template>
  <div class="container">
    <div>
      <textarea v-model="message" placeholder="add multiple lines"></textarea>
      <InkButton />
      <button v-on:click="send">言葉を色付ける</button>
      <div id="result">
        <div id="result_color" class="result_color">{{ message_color }}</div>
        <div id="result_message">{{ message }}</div>
      </div>
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
.container {
  width:80%;
  margin: 0 auto;
  min-height: 100vh;
  display: flex;
  justify-content: center;
  align-items: center;
  text-align: center;
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
}

.result_color{
  height:40px;
  background: none;
  color:white;
}

</style>
