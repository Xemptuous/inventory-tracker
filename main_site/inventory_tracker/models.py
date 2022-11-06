from django.db import models
from django.utils import timezone
import datetime as dt

# Main Division (Game name, Website name, etc.)
class Host(models.Model):
    name = models.CharField(max_length=255, null=False)
    description = models.TextField()

    def __str__(self):
        return self.name

# Secondary Division (savefiles, characters, etc.)
class SubHost(models.Model):
    name = models.CharField(max_length=255, null=False)
    description = models.TextField(null=True, blank=True)
    host = models.ForeignKey(Host, on_delete=models.CASCADE, null=False)

    def __str__(self):
        return self.name


# Item parent/derived categories
class ItemCategory(models.Model):
    name = models.CharField(max_length=255, null=False)
    host = models.ForeignKey(Host, on_delete=models.CASCADE)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name


class StructureCategory(models.Model):
    name = models.CharField(max_length=255, null=False)
    host = models.ForeignKey(Host, on_delete=models.CASCADE)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name


class Item(models.Model):
    name = models.CharField(max_length=255, null=False)
    host = models.ForeignKey(Host, on_delete=models.CASCADE)
    category = models.ForeignKey(ItemCategory, on_delete=models.CASCADE, null=True)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name


class Transaction(models.Model):
    subhost = models.ForeignKey(SubHost, on_delete=models.CASCADE, null=True)
    item_category = models.ForeignKey(ItemCategory, on_delete=models.CASCADE, null=True)
    structure_category = models.ForeignKey(StructureCategory, on_delete=models.CASCADE, null=True, blank=True)
    item = models.ForeignKey(Item, on_delete=models.CASCADE, null=True)
    buy_qty = models.IntegerField(null=True, blank=True)
    buy_price = models.FloatField(null=True, blank=True)
    buy_loc = models.CharField(max_length=255, default=None, null=True, blank=True)
    buy_ts = models.DateTimeField('date purchased', null=True, blank=True)
    sell_qty = models.IntegerField(null=True, blank=True)
    sell_price = models.FloatField(null=True, blank=True)
    sell_loc = models.CharField(max_length=255, default=None, null=True, blank=True)
    sell_ts = models.DateTimeField('date sold', null=True, blank=True)
    notes = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.item.name

    def is_recent_purchase(self):
        return self.buy_ts >= timezone.now() - dt.timedelta(days=1)

    def is_recent_sale(self):
        return self.sell_ts >= timezone.now() - dt.timedelta(days=1)

    def is_completed_transaction(self):
        return self.buy_ts is not None and self.sell_ts is not None

    def is_purchase(self):
        return self.buy_qty is not None

    def is_sale(self):
        return self.sell_qty is not None

    def latest_timestamp(self):
        return self.buy_ts if self.buy_ts is not None else self.sell_ts

    def total_qty(self):
        if self.buy_qty and not self.sell_qty:
            return self.buy_qty
        elif self.sell_qty and not self.buy_qty:
            return self.sell_qty
        return models.F(self.buy_qty) + models.F(self.sell_qty)


class Structure(models.Model):
    name = models.CharField(max_length=255, null=False)
    description = models.TextField(null=True, blank=True)
    host = models.ForeignKey(Host, on_delete=models.CASCADE, null=False)
    category = models.ForeignKey(StructureCategory, on_delete=models.CASCADE, null=True)
    buy_qty = models.IntegerField(null=True, blank=True)
    buy_price = models.FloatField(null=True, blank=True)
    buy_loc = models.CharField(max_length=255, default=None, null=True)
    buy_ts = models.DateTimeField('date purchased', null=True, blank=True)
    sell_qty = models.IntegerField(null=True, blank=True)
    sell_price = models.IntegerField(null=True, blank=True)
    sell_loc = models.CharField(max_length=255, default=None, null=True)
    sell_ts = models.DateTimeField('date sold', null=True, blank=True)
    # cycle_time = models.DurationField(null=True, blank=True)

    # production / outputs
    item_output_one = models.ForeignKey(Item, on_delete=models.CASCADE, null=True, related_name="item_output_one")
    num_output_one = models.FloatField(null=True, blank=True)
    time_output_one = models.DurationField(null=True, blank=True)
    item_output_two = models.ForeignKey(Item, on_delete=models.CASCADE, null=True, related_name="ete")
    num_output_two = models.FloatField(null=True, blank=True)
    time_output_two = models.DurationField(null=True, blank=True)
    item_output_three = models.ForeignKey(Item, on_delete=models.CASCADE, null=True, related_name="item_output_three")
    num_output_three = models.FloatField(null=True, blank=True)
    time_output_three = models.DurationField(null=True, blank=True)
    item_output_four = models.ForeignKey(Item, on_delete=models.CASCADE, null=True, related_name="item_output_four")
    num_output_four = models.FloatField(null=True, blank=True)
    time_output_four = models.DurationField(null=True, blank=True)
    item_output_five = models.ForeignKey(Item, on_delete=models.CASCADE, null=True, related_name="item_output_five")
    num_output_five = models.FloatField(null=True, blank=True)
    time_output_five = models.DurationField(null=True, blank=True)
    item_output_six = models.ForeignKey(Item, on_delete=models.CASCADE, null=True, related_name="item_output_six")
    num_output_six = models.FloatField(null=True, blank=True)
    time_output_six = models.DurationField(null=True, blank=True)

    # resources / inputs
    item_input_one = models.ForeignKey(Item, on_delete=models.CASCADE, null=True, related_name="item_input_one")
    consume_input_one = models.FloatField(null=True, blank=True)
    time_input_one = models.DurationField(null=True, blank=True)
    item_input_two = models.ForeignKey(Item, on_delete=models.CASCADE, null=True, related_name="item_input_two")
    consume_input_two = models.FloatField(null=True, blank=True)
    time_input_two = models.DurationField(null=True, blank=True)
    item_input_three = models.ForeignKey(Item, on_delete=models.CASCADE, null=True, related_name="item_input_three")
    consume_input_three = models.FloatField(null=True, blank=True)
    time_input_three = models.DurationField(null=True, blank=True)
    item_input_four = models.ForeignKey(Item, on_delete=models.CASCADE, null=True, related_name="item_input_four")
    consume_input_four = models.FloatField(null=True, blank=True)
    time_input_four = models.DurationField(null=True, blank=True)
    item_input_five = models.ForeignKey(Item, on_delete=models.CASCADE, null=True, related_name="item_input_five")
    consume_input_five = models.FloatField(null=True, blank=True)
    time_input_five = models.DurationField(null=True, blank=True)
    item_input_six = models.ForeignKey(Item, on_delete=models.CASCADE, null=True, related_name="item_input_six")
    consume_input_six = models.FloatField(null=True, blank=True)
    time_input_six = models.DurationField(null=True, blank=True)

    notes = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name


