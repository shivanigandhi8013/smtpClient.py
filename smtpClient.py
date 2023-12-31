from socket import *


def smtp_client(port=1025, mailserver='127.0.0.1'):
    msg = "\r\n My message"
    endmsg = "\r\n.\r\n"

    # Choose a mail server (e.g. Google mail server) if you want to verify the script beyond GradeScope

    # Create socket called clientSocket and establish a TCP connection with mailserver and port

    # Fill in start
    clientSocket = socket(AF_INET, SOCK_STREAM)
    clientSocket.connect((mailserver,port))


    # Fill in end

    recv = clientSocket.recv(1024).decode()
    #print(recv) #You can use these print statement to validate return codes from the server. #hash ouut
    #if recv[:3] != '220':
    #    print('220 reply not received from server.')

    # Send HELO command and print server response.
    heloCommand = 'HELO Alice\r\n'
    clientSocket.send(heloCommand.encode())
    recv1 = clientSocket.recv(1024).decode()
    #print(recv1) #hash out
    #if recv1[:3] != '250':  #hash out
        #print('250 reply not received from server.')  #hash out

    # Send MAIL FROM command and handle server response.
    # Fill in start
    mailfromCommand = 'MAIL FROM:<shivani@gmail.com>\r\n'
    clientSocket.send(mailfromCommand.encode())
    recv2 = clientSocket.recv(1024).decode()
    if recv2[:3] != '250':  #hash out
        print('MAIL FROM command not received from server.')  #hash out


    # Fill in end

    # Send RCPT TO command and handle server response.
    # Fill in start
    rcpttoCommand = 'RCPT TO:<gandhi@gmail.com>\r\n'
    clientSocket.send(rcpttoCommand.encode())
    recv3 = clientSocket.recv(1024).decode()
    if recv3[:3] != '250':  #hash out
        print('RCPT TO command not received from server.')  #hash out
    #if recv3[:3] != '251':
        #print('RCPT TO command not received from server.')  # hash out
    # Fill in end

    # Send DATA command and handle server response.
    # Fill in start
    dataCommand = 'DATA\r\n'
    clientSocket.send(dataCommand.encode())
    recv4 = clientSocket.recv(1024).decode('utf-8')
    #if recv4[:3] == '354':  # hash out
    #print(recv4)  # hash out
    # Fill in end

    # Send message data.
    # Fill in start
    clientSocket.send(msg.encode())
    # Fill in end

    # Message ends with a single period, send message end and handle server response.
    # Fill in start
    clientSocket.send(endmsg.encode())
    recv5 = clientSocket.recv(1024).decode()

    # Fill in end

    # Send QUIT command and handle server response.
    # Fill in start

    quitCommand = 'QUIT\r\n'
    clientSocket.send(quitCommand.encode())
    recv5 = clientSocket.recv(1024).decode()
    #if recv5[:3] == '221':  # hash out
        #print('QUIT') # hash out

    clientSocket.close()

    # Fill in end


if __name__ == '__main__':
    smtp_client(1025, '127.0.0.1')
