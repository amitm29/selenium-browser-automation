from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import re

scoreRegex = re.compile(r'\d+')

browser = webdriver.Firefox()
browser.get('https://gabrielecirulli.github.io/2048/')

best_score = 0
total_score = 0
trials = 10
t_no = 0

def play_game(tno):
	htmlElem = browser.find_element_by_tag_name('html')
	elem = browser.find_element_by_css_selector('.game-message')
	

	while not elem.is_displayed():
		score_elem = browser.find_element_by_css_selector('.score-container')

		sc = int(scoreRegex.search(score_elem.text).group(0))
		s = -10

		while s < int(scoreRegex.search(score_elem.text).group(0)):
			s = int(scoreRegex.search(score_elem.text).group(0))
			htmlElem.send_keys(Keys.DOWN)
			htmlElem.send_keys(Keys.RIGHT)
		else:
			htmlElem.send_keys(Keys.UP)

		if sc == int(scoreRegex.search(score_elem.text).group(0)):
			htmlElem.send_keys(Keys.LEFT)

	else:
		
		print(f'Trial# : {tno}		Score : {int(score_elem.text)}')	
		return int(score_elem.text)


if __name__=='__main__':
	print("Starting the game.....")
	for i in range(trials):
		t_no = t_no + 1
		score = play_game(t_no)
		if score > best_score:
			best_score = score
		total_score = total_score + score
		print(f'Avg : {total_score/t_no}\n')

	print(f'Best score : {best_score}')
	print(f'Average score : {total_score/trials}')

	retry_btn = browser.find_element_by_css_selector('.retry-button')
	retry_btn.click()
