class AddIndexToTerms < ActiveRecord::Migration
  def change
    add_index :terms, :term
  end
end
