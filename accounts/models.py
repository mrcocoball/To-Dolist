from django.db import models
from django.contrib.auth.models import AbstractUser

# 랭크
class RankChoice(models.TextChoices):
    BRONZE = u'BRONZE', 'BRONZE'
    SILVER = u'SILVER', 'SILVER'
    GOLD = u'GOLD', 'GOLD'
    PLATINUM = u'PLATINUM', 'PLATINUM'
    DIAMOND = u'DIAMOND', 'DIAMOND'
    MASTER = u'MASTER', 'MASTER'

class User(AbstractUser):
    
    username = models.CharField(max_length=15, unique=True, error_messages={"unique" : "이미 존재하는 닉네임입니다."})
    first_name = None
    last_name = None
    todo_count = models.BigIntegerField('TODO_COUNT', null=True, default=0)
    todo_complete_count = models.BigIntegerField('TODO_COMPLETE_COUNT', null=True, default=0)
    rank = models.CharField('RANK', max_length=10, choices=RankChoice.choices, default=RankChoice.BRONZE, null=True)
    social = models.BooleanField('SOCIAL', default=False)

    # 랭크 관련 지표
    SILVER_REQUIRED_TODO_COUNT = 10
    SILVER_REQUIRED_TODO_COMPLETE_COUNT = 5
    GOLD_REQUIRED_TODO_COUNT = 30
    GOLD_REQUIRED_TODO_COMPLETE_COUNT = 15
    PLATINUM_REQUIRED_TODO_COUNT = 100
    PLATINUM_REQUIRED_TODO_COMPLETE_COUNT = 50
    DIAMOND_REQUIRED_TODO_COUNT = 200
    DIAMOND_REQUIRED_TODO_COMPLETE_COUNT = 150
    MASTER_REQUIRED_TODO_COUNT = 400
    MASTER_REQUIRED_TODO_COMPLETE_COUNT = 300

    def __str__(self):
        return self.email
    
    def plus_todo_count(self):
        self.todo_count += 1
        self.level_up_check()
        self.save()

    def plus_todo_complete_count(self):
        self.todo_complete_count += 1
        self.level_up_check()
        self.save()

    def level_up_check(self):
        if self.rank == "BRONZE":
            if self.todo_count >= self.SILVER_REQUIRED_TODO_COUNT:
                if self.todo_complete_count >= self.SILVER_REQUIRED_TODO_COMPLETE_COUNT:
                    self.level_up()            
        elif self.rank == "SILVER":
            if self.todo_count >= self.GOLD_REQUIRED_TODO_COUNT:
                if self.todo_complete_count >= self.GOLD_REQUIRED_TODO_COMPLETE_COUNT:
                    self.level_up()
        elif self.rank == "GOLD":
            if self.todo_count >= self.PLATINUM_REQUIRED_TODO_COUNT:
                if self.todo_complete_count >= self.PLATINUM_REQUIRED_TODO_COMPLETE_COUNT:
                    self.level_up()
        elif self.rank == "PLATINUM":
            if self.todo_count >= self.DIAMOND_REQUIRED_TODO_COUNT:
                if self.todo_complete_count >= self.DIAMOND_REQUIRED_TODO_COMPLETE_COUNT:
                    self.level_up()
        elif self.rank == "DIAMOND":
            if self.todo_count >= self.MASTER_REQUIRED_TODO_COUNT:
                if self.todo_complete_count >= self.MASTER_REQUIRED_TODO_COMPLETE_COUNT:
                    self.level_up()                    
        else:
            pass

    def level_up(self):
        if self.rank == "BRONZE":
            self.rank = "SILVER"
        elif self.rank == "SILVER":
            self.rank = "GOLD"
        elif self.rank == "GOLD":
            self.rank = "PLATINUM"
        elif self.rank == "PLATINUM":
            self.rank = "DIAMOND"
        elif self.rank == "DIAMOND":
            self.rank = "MASTER"
        else:
            pass

